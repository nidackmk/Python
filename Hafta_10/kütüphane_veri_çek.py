cryptocmd'den  CmcScraper'ı  içe  aktarın

# kazıyıcıyı zaman aralığı ile başlat
kazıyıcı  =  CmcScraper ( "XRP" , "15-10-2017" , "25-10-2017" )

# ham verileri liste listesi olarak al
başlıklar , veri  =  kazıyıcı . get_data ()

# verileri json formatında al
json_data  =  kazıyıcı . get_data ( "json" )

# verileri csv'ye aktar
kazıyıcı _ dışa aktarma ( "csv" )

# veriler için veri çerçevesini al
df  =  kazıyıcı _ get_dataframe ()