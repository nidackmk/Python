isteklerden  import  İstek , Oturum _
 isteklerden . _ istisnalar  içe aktarma  ConnectionError , Timeout , TooManyRedirects
 json'u içe aktar

url  =  'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parametreler  = {
  'başlangıç' : '1' ,
  'sınır' : '5000' ,
  'dönüştür' : 'USD'
}
başlıklar  = {
  'Kabul Ediyor' : 'uygulama/json' ,
  'X-CMC_PRO_API_KEY' : 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c' ,
}

oturum  =  Oturum ()
oturum _ başlıklar _ güncelleme ( başlıklar )

deneyin :
  yanıt  =  oturum _ get ( url , parametreler = parametreler )
  veri  =  json . yükler ( yanıt . metin )
  yazdır ( veri )
hariç ( ConnectionError , Timeout , TooManyRedirects ) as  e :
  yazdır ( e )