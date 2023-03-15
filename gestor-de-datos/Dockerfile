# se inicia con una imagen de python
FROM python:3.8-alpine

# se crea la carpeta que contendrá el código
RUN mkdir /gestor-de-datos

# se copia el código del microservicio dentro de la carpeta creada
ADD . /gestor-de-datos

# se mueve a la carpeta creada
WORKDIR /gestor-de-datos

# se instalan las dependencias del microservicio
RUN pip install -r requirements.txt

# se ejecuta el archivo principal del componente
CMD ["python", "loader.py"]