start:
		ipython3 main.py



# Удаление Docker контейнера
remove-container:
		docker rm chatbot

# Запуск контейнера
run-container:
		docker run -d --name chatbot -p 5434:5432 -e POSTGRES_PASSWORD=password postgres
# Остановка и перезапуск контейнера
stop-container:
		docker stop chatbot

start-container:
		docker start chatbot

#Запуск sql скриптов внутри докер контейнера 
run-sql-scripts:
		
