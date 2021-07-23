//PINES PARA EL MOTOR DERECHO
#define motorDA 5
#define motorDR 6

//PINES PARA EL MOTOR IZQUIERDO
#define motorIA 9
#define motorIR 10

//ULTRASONICO
#define trig 2
#define echo0 3

//ASPIRADORA
#define aspi 40

//DECALRACION DE VARIABLES
int b='D',c, x, y, z, a=0, i=0;
float distancia0;

void setup() {
  // SE INICIALIZA LA VELOCIDAD DE LA COMUNICACION UART PARA EL BLUETOOTH
  Serial.begin(9600);

  //DECLARA EL MODO DE LOS PINES
  pinMode(trig, OUTPUT);
  pinMode(echo0,INPUT);
  pinMode(motorDA,OUTPUT);
  pinMode(motorDR,OUTPUT);
  pinMode(motorIA,OUTPUT);
  pinMode(motorIR,OUTPUT);
  digitalWrite(trig,LOW);

}

void loop() {
  // LEE EL DATO ENVIADO AL UART
  if(Serial.available()>0){
    b=Serial.read();
    if(b=='M'){
      c='M';
      detener();
      }
    if(b=='P'){
      c='P';
      detener();
      }
    if(b=='N'){
      c='N';
      detener();
      }
    }

    envia_dato();
    x=pulseIn(echo0,HIGH);
    distancia0=x/58;
    //Serial.println(x);
    Serial.println(String(distancia0)+"cm");

    if(c=='M'){

    if(distancia0<=5)
    {
      reversa();
      delay(1000);
      detener();
      delay(200);
      i=a%2;
      a++;
      if(i==0)
      {
        g_adelante_derecha();
        delay(1000);
        adelante();
        
      }
      else
      {
        g_adelante_izquierda();
        delay(1000);
        adelante();
      }
    }


    //DETENER MOTORES
    if(b=='D'){
      detener();
      }
    //IR HACIA ADELANTE
    if(b=='A'){
      adelante();
    }
    //IR DE REVERSA
    if(b=='R'){
      reversa();
    }
    //GIRAR ADELANTE A LA IZQUIERDA
    if(b=='G'){
      g_adelante_izquierda();
      delay(500);
      adelante();
    }
    //GIRAR DE REVERSA A LA IZQUIERDA
    if(b=='J'){
      g_reversa_izquierda();
      delay(500);
      reversa();
    }
    //GIRAR ADELANTE A LA DERECHA
    if(b=='H'){
      g_adelante_derecha();
      delay(500);
      adelante();
    }
    //GIRAR DE REVERSA HACIA LA DERECHA
    if(b=='K'){
      g_reversa_derecha();
      delay(500);
      reversa();
    }
    //Gira 90° Izquierda
    if(b=='I'){
      g_adelante_izquierda();
      delay(1000);
      adelante();
      }
    //Gira 90° Derecha
    if(b=='C'){
      g_adelante_derecha();
      delay(1000);
      adelante();
      }
    }

    if(c=='P'){

      if(distancia0<=5)
    {
      reversa();
      delay(500);
      detener();
      delay(200);
      i=a%2;
      a++;
      if(i==0)
      {
        g_adelante_derecha();
        delay(500);
        adelante();
        
      }
      else
      {
        g_adelante_izquierda();
        delay(500);
        adelante();
      }
    }

    adelante();
    
    }

}

//FUNCIONES DE DIRECCIONES DEL CARRITO
void envia_dato()
{
  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
}
void adelante()
{ 
  digitalWrite(motorDA,50);
  digitalWrite(motorIA,50);
  digitalWrite(motorDR,0);
  digitalWrite(motorIR,0); 
}
void reversa()
{ 
  digitalWrite(motorDA,0);
  digitalWrite(motorIA,0);
  digitalWrite(motorDR,50);
  digitalWrite(motorIR,50); 
}
void g_adelante_derecha()
{ 
  digitalWrite(motorDA,0);
  digitalWrite(motorIA,70);
  digitalWrite(motorDR,70);
  digitalWrite(motorIR,0); 
}
void g_adelante_izquierda()
{ 
  digitalWrite(motorDA,70);
  digitalWrite(motorIA,0);
  digitalWrite(motorDR,0);
  digitalWrite(motorIR,70); 
}
void g_reversa_derecha()
{ 
  digitalWrite(motorDA,0);
  digitalWrite(motorIA,0);
  digitalWrite(motorDR,0);
  digitalWrite(motorIR,80); 
}
void g_reversa_izquierda()
{ 
  digitalWrite(motorDA,0);
  digitalWrite(motorIA,0);
  digitalWrite(motorDR,80);
  digitalWrite(motorIR,0); 
}
void detener()
{ 
  digitalWrite(motorDA,0);
  digitalWrite(motorIA,0);
  digitalWrite(motorDR,0);
  digitalWrite(motorIR,0); 
}
