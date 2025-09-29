FROM base
LABEL maintainer="LAN-slide"

RUN apt-get update && apt-get install -y curl

RUN mkdir /amxx/

WORKDIR /amxx

ARG metamod_r_url="https://github.com/rehlds/Metamod-R/releases/download/1.3.0.149/"
ARG metamod_r="metamod-bin-1.3.0.149.zip"
#ARG metamod_r="metamod.zip"

ARG url_stable="https://www.amxmodx.org/release/"
ARG url_dev="https://www.amxmodx.org/amxxdrop/1.9/"
ARG metamod="metamod-1.21.1-am.zip"
ARG amxmodx_base_stable="amxmodx-1.8.2-base-linux.tar.gz"
ARG amxmodx_cs_stable="amxmodx-1.8.2-cstrike-linux.tar.gz"
ARG amxmodx_base_dev="amxmodx-1.9.0-git5294-base-linux.tar.gz"
ARG amxmodx_cs_dev="amxmodx-1.9.0-git5294-cstrike-linux.tar.gz"
ARG rehlds_url="https://github.com/rehlds/ReHLDS/releases/download/3.13.0.788/"
ARG rehlds="rehlds-bin-3.13.0.788.zip"
#ARG rehlds="rehlds.zip"
ARG regamedllcs_url="https://github.com/rehlds/ReGameDLL_CS/releases/download/5.26.0.668/"
ARG regamedllcs="regamedll-bin-5.26.0.668.zip"
#ARG regamedllcs="regamedllcs.zip"
ARG matchbot_url="https://github.com/SmileYzn/MatchBot/releases/download/1.0.4/"
ARG matchbot="linux32.zip"

ARG match_deluxe_url="https://forums.alliedmods.net/attachment.php?attachmentid=17394&d=1182746512"
ARG match_deluxe="amx_match_deluxe_811.zip"
ARG match_deluxe_cfg="match-deluxe/addons/amxmodx/configs/amxmd/amxmd.cfg"

#ARG pugmod_url="https://forums.alliedmods.net/attachment.php?attachmentid=181983&d=1640182982"
#ARG pugmod="PugMod-master.zip"
#ARG pugmod_url="https://hl2go.com/downloads/dedicated-servers/amx-mod-x/plugins/cs-pug-mod-4-0-2/?download=2483"
#ARG pugmod="pugmod.zip"

#RUN wget -nc "${url_stable}${metamod}" && unzip "${metamod}" && rm "${metamod}" -f
RUN wget -nc "${metamod_r_url}${metamod_r}" && unzip "${metamod_r}" && rm "${metamod_r}" -f
RUN wget -nc "${url_stable}${amxmodx_base_stable}" && tar -xzf "${amxmodx_base_stable}" && rm "${amxmodx_base_stable}" -f
RUN wget -nc "${url_stable}${amxmodx_cs_stable}" && tar -xzf "${amxmodx_cs_stable}" && rm "${amxmodx_cs_stable}" -f

#RUN echo "linux addons/amxmodx/dlls/amxmodx_mm_i386.so" > "addons/metamod/plugins.ini"


RUN wget -nc "${rehlds_url}${rehlds}" && unzip "${rehlds}" -d rehlds && rm "${rehlds}" -f
RUN wget -nc "${regamedllcs_url}${regamedllcs}" && unzip "${regamedllcs}" -d regamedllcs && rm "${regamedllcs}" -f
#RUN wget -nc "${matchbot_url}${matchbot}" && unzip "${matchbot}" -d matchbot && rm "${matchbot}" -f

#RUN rm matchbot/addons/metamod -rf
#RUN rm matchbot/liblist.gam -f

#UN wget "${pugmod_url}" -O ${pugmod} && unzip ${pugmod} "PugMod-master/*" && rm "${pugmod}" -f
#RUN curl -o ${pugmod} -OJL "${pugmod_url}" && unzip ${pugmod} && rm "${pugmod}" -f

RUN wget -nc "${match_deluxe_url}" -O "${match_deluxe}" && unzip "${match_deluxe}" -d "match-deluxe" && rm "${match_deluxe}" -f
RUN sed -i 's|amx_match_hostname "1"|amx_match_hostname "0"|g' "${match_deluxe_cfg}"
RUN sed -i 's|amx_match_password "1"|amx_match_password "0"|g' "${match_deluxe_cfg}"
RUN sed -i 's|amx_match_password2 "scrim"|amx_match_password2 ""|g' "${match_deluxe_cfg}"
RUN sed -i 's|amx_match_pugstyle "0"|amx_match_pugstyle "1"|g' "${match_deluxe_cfg}"

COPY config_admins.py /amxx
COPY plugins.ini /amxx/addons/metamod/
