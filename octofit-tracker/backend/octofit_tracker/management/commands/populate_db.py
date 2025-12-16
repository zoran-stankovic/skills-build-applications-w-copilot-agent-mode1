
from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import connection
from pymongo import ASCENDING

class Command(BaseCommand):
	help = 'Populate the octofit_db database with test data'

	def handle(self, *args, **options):
		self.stdout.write(self.style.SUCCESS('Connecting to MongoDB...'))
		db = connection.cursor().db_client[settings.DATABASES['default']['NAME']]

		# Drop collections if they exist
		for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
			db[col].drop()

		# Users (superheroes)
		users = [
			{"name": "Tony Stark", "email": "ironman@marvel.com", "team": "marvel"},
			{"name": "Steve Rogers", "email": "cap@marvel.com", "team": "marvel"},
			{"name": "Bruce Wayne", "email": "batman@dc.com", "team": "dc"},
			{"name": "Clark Kent", "email": "superman@dc.com", "team": "dc"},
		]
		db.users.insert_many(users)
		db.users.create_index([("email", ASCENDING)], unique=True)

		# Teams
		teams = [
			{"name": "marvel", "members": ["ironman@marvel.com", "cap@marvel.com"]},
			{"name": "dc", "members": ["batman@dc.com", "superman@dc.com"]},
		]
		db.teams.insert_many(teams)

		# Activities
		activities = [
			{"user_email": "ironman@marvel.com", "activity": "Running", "duration": 30},
			{"user_email": "cap@marvel.com", "activity": "Cycling", "duration": 45},
			{"user_email": "batman@dc.com", "activity": "Martial Arts", "duration": 60},
			{"user_email": "superman@dc.com", "activity": "Flying", "duration": 120},
		]
		db.activities.insert_many(activities)

		# Leaderboard
		leaderboard = [
			{"team": "marvel", "points": 150},
			{"team": "dc", "points": 180},
		]
		db.leaderboard.insert_many(leaderboard)

		# Workouts
		workouts = [
			{"name": "HIIT", "difficulty": "hard"},
			{"name": "Yoga", "difficulty": "easy"},
		]
		db.workouts.insert_many(workouts)

		self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
