FROM ich777/altitude

COPY --chown=altitude:altitude data /altitude
COPY --chown=altitude:altitude launcher_config.xml /altitude/servers/
COPY --chown=altitude:altitude entrypoint.sh /opt/scripts/

RUN chmod +x /opt/scripts/entrypoint.sh

ENTRYPOINT /opt/scripts/entrypoint.sh
