docker-compose down -v  
docker-compose up -d  
docker ps  

docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092  
docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --describe --topic orders  