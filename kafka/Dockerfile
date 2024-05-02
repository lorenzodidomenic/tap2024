FROM amazoncorretto:17
LABEL maintainer="Salvo Nicotra"
#variabili d'amabienre che uso in fase di settaggio dell'immagine 
ENV PATH /opt/kafka/bin:$PATH
ENV KAFKA_DIR "/opt/kafka"
ARG KAFKA_VERSION="2.13-3.7.0"

#aggiungo e scompatto il software kafka alla directory otp, ovvero lo installo 
ADD setup/kafka_${KAFKA_VERSION}.tgz /opt

# Create Symbolik Link 
RUN ln -s /opt/kafka_${KAFKA_VERSION} ${KAFKA_DIR} 
#metto il file kafka-manager.sh definito in locale all'intenro di /opt/kafka/bin/kafka-manager
ADD kafka-manager.sh ${KAFKA_DIR}/bin/kafka-manager
# Copy All conf all'interno di config
ADD conf/* ${KAFKA_DIR}/config/

#eseguo al lancio del container kafka-manager al quale passerò le opzioni
ENTRYPOINT [ "kafka-manager" ]