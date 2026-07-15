import qrcode
import csv


print("Iniciando a geração dos QR Codes...\n")

with open('dados.csv', mode='r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    
    
    for linha in leitor:
      
        if not linha:
            continue
            
        nome_do_arquivo = linha[0] 
        link_do_docs = linha[1]    
        
        print(f"-> Gerando: {nome_do_arquivo}.png")
        
        QR = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        QR.add_data(link_do_docs)
        QR.make(fit=True)
        
        imagem = QR.make_image(fill_color="black", back_color="white")
        
        # Salva a imagem usando o nome que estava na planilha
        imagem.save(f"{nome_do_arquivo}.png")

print("\nSucesso! Todos os QR Codes foram gerados.")