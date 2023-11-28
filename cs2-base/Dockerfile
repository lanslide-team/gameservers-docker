#FROM wine
FROM base

RUN useradd -m steam && mkdir /cs2 && chown steam:steam /cs2

ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true

USER steam
WORKDIR /cs2

#COPY data ./
COPY --chown=steam:steam data ./
COPY --chown=steam:steam steamclient.so /home/steam/.steam/sdk64/steamclient.so
