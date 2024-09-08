start:
		ipython3 main.py



# Удаление Docker контейнера
remove-container:
		docker rm chatbot

# Запуск контейнера
run-container:
		docker run -d --name chatbot -p 5434:5432 -e POSTGRES_PASSWORD=password postgres
	$(PWD)/sql_scripts:/sql_scripts postgres
# остановка и перезапуск контейнера
stop-container:
		docker stop chatbot

start-container:
		docker start chatbot

# Выполнение всех SQL скриптов
.PHONY: run-sql-scripts
run-sql-scripts:
		for script in /sql_scripts/*.sql; do \
			docker exec -i chatbot psql -U postgres -d postgres -f $$script; \
		done
