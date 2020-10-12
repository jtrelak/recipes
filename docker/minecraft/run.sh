docker build -t minecraft_gui .
docker run \
    --device=/dev/dri \
    --group-add video \
    --network=host \
    --volume=/tmp/.X11-unix:/tmp/.X11-unix \
    --env="DISPLAY=$DISPLAY" -h $HOSTNAME -v $HOME/.Xauthority:/home/jtrelak/.Xauthority minecraft_gui
