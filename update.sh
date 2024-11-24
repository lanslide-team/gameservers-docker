#!/bin/bash
    
declare gs_root
gs_root=`pwd`

csgo_surf() {
    declare gs_root=$1
    declare maps_url="https://lanslide.com.au/storage/csgo/maps"
    declare surf_root=csgo-surf
    declare maps_folder=maps

    wget -nc "$maps_url/surf_colours.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_colours.nav" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_cubic.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_edge.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_edge.nav" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_forbidden_ways_ksf.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_how2surf.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_kitsune.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_luna2_.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_luna2_.nav" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_lux.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_nyx.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_pantheon.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_resort_jk.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_tendies.bsp" -P $gs_root/$surf_root/$maps_folder/
    wget -nc "$maps_url/surf_training.bsp" -P $gs_root/$surf_root/$maps_folder/
}

doom2() {
    declare gs_root=$1
    declare doom2_root="zdaemon"
    declare sub_folder="wads"
    declare wad_file="https://lanslide.com.au/storage/doom2/DOOM2.WAD"

    wget -nc $wad_file -P $gs_root/$doom2_root/$sub_folder
}

haloce() {
    declare gs_root=$1
    declare haloce_folder="haloce"
    declare git_repo="https://github.com/antimomentum/halopull.git"
    declare sub_folder="data"

    if [ -d $gs_root/$haloce_folder/$sub_folder ]; then
        cd $gs_root/$haloce_folder/$sub_folder && git pull 
    else
        git clone $git_repo $gs_root/$haloce_folder/$sub_folder
    fi
}

mc() {
    declare gs_root=$1
    declare mc_server_root="https://github.com/mango63/Docker_Spigot-Minecraft"
    declare mc_build="minecraft-build"
    declare mc_survival="minecraft-survival"

    # MC creative build
    if [ -d $gs_root/$mc_build ]; then
        svn update $gs_root/$mc_build
    else
        svn checkout $mc_server_root/trunk/$mc_build
    fi	
    
    # MC survival build
    if [ -d $gs_root/$mc_survival ]; then
        svn update $gs_root/$mc_survival
    else
        svn checkout $mc_server_root/trunk/$mc_survival
    fi	
}

mc_vols() {
    mkdir -p /opt/minecraft/creative/plotworld
    mkdir -p /opt/minecraft/survival/world
    chmod 777 /opt/minecraft -R
}

tmf() {
    declare gs_root=$1
    declare server_zip_file="TrackmaniaServer_2011-02-21.zip"
    declare tmf_folder="trackmania-forever"
    declare tmf_rcon_folder="trackmania-forever-rcon"
    declare tmf_remote_control_examples="RemoteControlExamples"

    wget -nc http://files2.trackmaniaforever.com/$server_zip_file -P $gs_root/$tmf_folder/
    wget -nc https://github.com/Chris92de/AdminServ/archive/refs/heads/master.zip -O $gs_root/$tmf_folder/AdminServ.zip

    # Download rcon tool
    if [ -d $gs_root/$tmf_rcon_folder ]; then
        svn update $gs_root/$tmf_rcon_folder
    else
        svn checkout https://github.com/OpenSourceLAN/gameservers-docker/trunk/trackmania-forever-rcon $gs_root/$tmf_rcon_folder
    fi

    # Copy across rcon examples
    if [ ! -d $gs_root/$tmf_rcon_folder/$tmf_remote_control_examples ]; then
        unzip "$gs_root/$tmf_folder/$server_zip_file" "$tmf_remote_control_examples/*" -d $gs_root/$tmf_rcon_folder
    fi
}

ut99() {
    declare gs_root=$1
    declare ut_server_root="https://github.com/Roemer/ut99-server"
    declare ut_folder="ut99"
    declare sub_folder="data"

    if [ -d $gs_root/$ut_folder/$sub_folder ]; then
        svn update $gs_root/$ut_folder/$sub_folder
    else
        svn checkout $ut_server_root/trunk/$sub_folder $gs_root/$ut_folder/$sub_folder
    fi
}



tmf() {
    declare gs_root=$1
    declare server_zip_file="TrackmaniaServer_2011-02-21.zip"
    declare tmf_folder="trackmania-forever"
    declare tmf_rcon_folder="trackmania-forever-rcon"
    declare tmf_remote_control_examples="RemoteControlExamples"

    wget -nc http://files2.trackmaniaforever.com/$server_zip_file -P $gs_root/$tmf_folder/
    wget -nc https://github.com/Chris92de/AdminServ/archive/refs/heads/master.zip -O $gs_root/$tmf_folder/AdminServ.zip

    # Download rcon tool
    if [ -d $gs_root/$tmf_rcon_folder ]; then
        svn update $gs_root/$tmf_rcon_folder
    else
        svn checkout https://github.com/OpenSourceLAN/gameservers-docker/trunk/trackmania-forever-rcon $gs_root/$tmf_rcon_folder
    fi

    # Copy across rcon examples
    if [ ! -d $gs_root/$tmf_rcon_folder/$tmf_remote_control_examples ]; then
        unzip "$gs_root/$tmf_folder/$server_zip_file" "$tmf_remote_control_examples/*" -d $gs_root/$tmf_rcon_folder
    fi
}

ut99() {
    declare gs_root=$1
    declare ut_server_root="https://github.com/Roemer/ut99-server"
    declare ut_folder="ut99"
    declare sub_folder="data"

    if [ -d $gs_root/$ut_folder/$sub_folder ]; then
        svn update $gs_root/$ut_folder/$sub_folder
    else
        svn checkout $ut_server_root/trunk/files $gs_root/$ut_folder/$sub_folder
    fi
}

ut2004() {
    declare gs_root=$1
    declare ut2004_folder="ut2004"
    declare sub_folder="data"
#    declare server_files="https://archive.org/download/ut2004-server/dedicatedserver3369.3-bonuspack.zip"
    declare server_files="https://www.utzone.de/forum/downloads.php?do=file&id=1196&act=down"
    declare filename="dedicatedserver3369.3-bonuspack.7z"
    declare base_filename="dedicatedserver3369.3-bonuspack"

    #wget -nc $server_files -O $gs_root/$ut2004_folder/$filename && 
    ls $gs_root/$ut2004_folder/dedicatedserver*.7z >/dev/null || (
        w3m -dump_source "$server_files" >| $gs_root/$ut2004_folder/$filename
#        7za x $gs_root/$ut2004_folder/$filename -d $gs_root/$ut2004_folder/ && 
#	mv $gs_root/$ut2004_folder/$base_filename $gs_root/$ut2004_folder/$sub_folder &&
#	rm -f $gs_root/$ut2004_folder/$filename 
    )
}

zdaemon() {
    declare gs_root=$1
    declare zdaemon_folder="zdaemon"
    declare sub_folder="data" 
   
    ls $gs_root/$zdaemon_folder/zserv*linux26.tgz >/dev/null || (
        URL=$(curl -s https://www.zdaemon.org/?CMD=downloads | grep -o 'https://.*linux26.tgz' | head -n 1)
        wget -nc $URL  -O $gs_root/$zdaemon_folder/`basename $URL`
    )
}

steamcmd() {
    declare gs_root=$1

    declare steamcmd script username password
    declare -A games

    steamcmd="steamcmd"
    script="steamcmd.sh"
    target_folder="data"

    login="anonymous"
    login_user="stupidsteamlogin ssl_2022"

    # Declare games to update here
    games[cs-base]=90
    games[cs2-base]=730
    games[altitude]=41300
    games[7days]=294420
#    games[csgo-base]=740
    games[hl2]=232370
    games[l4d2]=222860
    games[reflex-arena]=329740
    games[retrocycles]=1306180
    games[rust]=258550
    games[tf2]=232250
    games[wreckfest]=361580

    ls ${gs_root}/${steamcmd}/${script} >/dev/null || (
        mkdir -p ${gs_root}/${steamcmd} &&
        wget -nc https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz -O ${gs_root}/${steamcmd}/steamcmd_linux.tar.gz &&
        tar -xvzf ${gs_root}/${steamcmd}/steamcmd_linux.tar.gz -C ${gs_root}/${steamcmd}/ && rm ${gs_root}/${steamcmd}/steamcmd_linux.tar.gz
    )

    for game in "${!games[@]}"
    do
        echo "Updating game [${game}]"
        if [ "${game}" = "altitude" -o "${game}" = "retrocycles" ]; then
            ${gs_root}/${steamcmd}/${script} +force_install_dir ${gs_root}/${game}/${target_folder} +login ${login_user} +app_update ${games[$game]} +quit
        elif [ "${game}" = "cs-base" ]; then
#            cp ${gs_root}/${steamcmd}/linux64/steamclient.so ${gs_root}/${game}/ -f 
	    ${gs_root}/${steamcmd}/${script} +force_install_dir ${gs_root}/${game}/${target_folder} +login ${login_user} +app_set_config ${games[$game]} mod cstrike +app_update ${games[$game]} -beta steam_legacy validate +quit
        elif [ "${game}" = "cs2-base" ]; then
            cp ${gs_root}/${steamcmd}/linux64/steamclient.so ${gs_root}/${game}/ -f 
	    ${gs_root}/${steamcmd}/${script} +force_install_dir ${gs_root}/${game}/${target_folder} +login ${login_user} +app_update ${games[$game]} +quit
        elif [ "${game}" = "wreckfest" -o "${game}" = "reflex-arena" ]; then
            ${gs_root}/${steamcmd}/${script} +force_install_dir ${gs_root}/${game}/${target_folder} +login ${login} +@sSteamCmdForcePlatformType windows +app_update ${games[$game]} +quit
        else
            ${gs_root}/${steamcmd}/${script} +force_install_dir ${gs_root}/${game}/${target_folder} +login ${login} +app_update ${games[$game]} +quit
        fi
    done

#    mv ${gs_root}/csgo-base/data/bin/libgcc_s.so.1 ${gs_root}/csgo-base/data/bin/libgcc_s.so.1.old
#    mv ${gs_root}/csgo-base/data/bin/libstdc++.so.6 ${gs_root}/csgo-base/data/bin/libstdc++.so.6.old
}

# CS:GO Surf maps
csgo_surf $gs_root

# Doom 2
doom2 $gs_root

# Halo CE
haloce $gs_root

# Minecraft volumes
mc_vols

# TrackMania Forever
tmf $gs_root

# Unreal Tournament 99 (GOTY)
ut99 $gs_root

# UT2004
ut2004 $gs_root

# Zdeamon
zdaemon $gs_root

# Steamcmd
steamcmd $gs_root

