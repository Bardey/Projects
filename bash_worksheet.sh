cat /home/dataguy/final_test/dilans_data.csv | grep 'buy' >> /home/dataguy/final_test/buy.csv
cat /home/dataguy/final_test/dilans_data.csv | grep 'subscribe' >> /home/dataguy/final_test/subscribe.csv
cat /home/dataguy/final_test/dilans_data.csv | grep 'read' >> /home/dataguy/final_test/read.csv
cat /home/dataguy/final_test/read.csv | grep -v 'SEO\|AdWords\|Reddit' >> /home/dataguy/final_test/read_returning.csv
cat /home/dataguy/final_test/read.csv | grep 'SEO\|AdWords\|Reddit' >> /home/dataguy/final_test/read_first.csv