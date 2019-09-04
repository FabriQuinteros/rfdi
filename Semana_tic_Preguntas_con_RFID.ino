#include <SPI.h>
#include <MFRC522.h>
#include<EEPROM.h>



#define RST_PIN  9    //Pin 9 para el reset del RC522
#define SS_PIN  10   //Pin 10 para el SS (SDA) del RC522
MFRC522 mfrc522(SS_PIN, RST_PIN); ///Creamos el objeto para el RC522

byte ActualUID[4]; //almacenará el código del Tag leído


void setup() {
  Serial.begin(9600); //Iniciamos La comunicacion serial
  SPI.begin();        //Iniciamos el Bus SPI
  mfrc522.PCD_Init(); // Iniciamos el MFRC522
}




void loop() {
  // Revisamos si hay nuevas tarjetas  presentes
  if ( mfrc522.PICC_IsNewCardPresent()) 
        {  
      //Seleccionamos una tarjeta
            if ( mfrc522.PICC_ReadCardSerial()) 
            {
                  // Enviamos serialemente su UID
                  for (byte i = 0; i < mfrc522.uid.size; i++) {
                    Serial.print(ActualUID[i]=mfrc522.uid.uidByte[i]);             
                  } 
                  Serial.println("");                    
                  
                  mfrc522.PICC_HaltA();
          
            }
      
  }
  
}
