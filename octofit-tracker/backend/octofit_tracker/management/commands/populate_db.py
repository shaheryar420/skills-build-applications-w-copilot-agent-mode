from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', password='thundergodpassword'),
            User(_id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', password='metalgeekpassword'),
            User(_id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers', password='zerocoolpassword'),
            User(_id=ObjectId(), email='crashoverride@hmhigh.edu', name='Natasha Romanoff', password='crashoverridepassword'),
            User(_id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team', members=[str(users[0]._id), str(users[1]._id)])
        team2 = Team(_id=ObjectId(), name='Gold Team', members=[str(users[2]._id), str(users[3]._id), str(users[4]._id)])
        team1.save()
        team2.save()

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], type='Cycling', duration=60, date='2025-04-09'),
            Activity(_id=ObjectId(), user=users[1], type='Crossfit', duration=120, date='2025-04-09'),
            Activity(_id=ObjectId(), user=users[2], type='Running', duration=90, date='2025-04-09'),
            Activity(_id=ObjectId(), user=users[3], type='Strength', duration=30, date='2025-04-09'),
            Activity(_id=ObjectId(), user=users[4], type='Swimming', duration=75, date='2025-04-09'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), team=team1, score=200),
            Leaderboard(_id=ObjectId(), team=team2, score=300),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))