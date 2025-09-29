FROM sourcemod
FROM css-base
LABEL maintainer="LAN-slide"

USER root
WORKDIR /css/

COPY --chown=steam:steam entrypoint.py /css/
COPY --from=sourcemod --chown=steam:steam /sm /css/cstrike

RUN git clone https://github.com/NOMFPS/Warmod-css-v91.git /warmod && rm /warmod/.git -rf && cp /warmod/* /css/cstrike -R && rm /warmod -rf

USER steam

RUN chmod +x /css/entrypoint.py
ENTRYPOINT ["./entrypoint.py"]
