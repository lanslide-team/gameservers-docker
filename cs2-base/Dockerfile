#FROM wine
FROM base

RUN useradd -lm steam && mkdir /cs2 && chown steam:steam /cs2

ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true

USER steam
WORKDIR /cs2

COPY --chown=steam:steam config_admins.py config_match.py config_server.py container.py ./
COPY --chown=steam:steam data ./
COPY --chown=steam:steam steamclient.so /home/steam/.steam/sdk64/steamclient.so
