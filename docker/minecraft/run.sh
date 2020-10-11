docker build -t minecraft_gui .
docker run --network=host -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -h $HOSTNAME -v $HOME/.Xauthority:/home/jtrelak/.Xauthority minecraft_gui
