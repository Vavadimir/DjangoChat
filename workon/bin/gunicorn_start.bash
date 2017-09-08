#!/bin/bash

NAME="DjangoChat"                                  # Name of the application
DJANGODIR=~/CourseNProgramming/Python/DjangoChat         # Django project directory
SOCKFILE=~/CourseNProgramming/Python/DjangoChat/run/gunicorn.sock  # we will communicte using this unix socket
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=DjangoChat.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=DjangoChat.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source workon/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec workon/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
