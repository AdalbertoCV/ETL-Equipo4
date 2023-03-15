# se inicia con una imagen de python
FROM python:3.8-alpine

# se crea la carpeta que contendrá el código
RUN mkdir /dashboard

# se copia el código del microservicio dentro de la carpeta creada
ADD . /dashboard

# se mueve a la carpeta creada
WORKDIR /dashboard

# se instalan dependencias complementarias de las librerias del componente
RUN apk --no-cache add musl-dev linux-headers g++

# se instalan las dependencias del componente
RUN pip install -r requirements.txt

# se ejecuta el archivo principal del componente
CMD ["python", "main.py"]