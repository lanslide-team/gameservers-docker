FROM base
MAINTAINER LAN-slide

RUN useradd steam && mkdir /rust && chown steam:steam /rust

USER steam

COPY --chown=steam:steam data /rust

WORKDIR /rust

# COPY --chown=steam:steam cfg/users.cfg /rust/server/lanslide/cfg/users.cfg
COPY --chown=steam:steam entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT /rust/entrypoint.sh
