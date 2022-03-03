#include <SPI.h>
#include <Ethernet.h>

byte mac[] = { 0x74,0x69,0x69,0x2D,0x30,0x5 }; //physical mac address
byte ip[] = { 60, 22, 84, 9 }; // ip in lan
byte gateway[] = { 60, 22, 84, 1 }; // internet access via router
byte subnet[] = { 255, 255, 255, 0 }; //subnet mask
EthernetServer server(80);
String readString;

// Relay state and pin
String relay1State = "Off";
const int relay = 7;

char linebuf[80];
int charcount=0;

void setup() { 

  pinMode(relay, OUTPUT);
  digitalWrite(relay, HIGH);  
  // Open serial communication at a baud rate of 9600
  Serial.begin(9600);
  
  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);
  server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());
}

void loop() {
   // Create a client connection
  EthernetClient client = server.available();
  if (!client) {
    return;
  }
 
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }

  String request = client.readStringUntil('\r');
  Serial.println(request); //print to serial monitor for debuging
  client.flush();

     ///////////////////// control arduino pin
     if (request.indexOf("/relay1off") > 0){
            digitalWrite(relay, HIGH);
            relay1State = "Off";
     }
     else if (request.indexOf("/relay1on") > 0){
            digitalWrite(relay, LOW);
            relay1State = "On";
     }

          client.println("HTTP/1.1 200 OK"); //send new page
          client.println("Content-Type: text/html");
          client.println();

          client.println("<HTML>");
          client.println("<HEAD>");
          client.println("<TITLE>Arduino Servo WEB</TITLE>");
          client.println("</HEAD>");
          client.println("<BODY>");
          client.println("<center>");

          client.println("<H1>Remote RCU POWER CONTROL MODULE_v1.1</H1>");      

          client.println("<p>'Choose the action you want'</p>");
          client.println("Current State :" + relay1State);         
          if(relay1State == LOW){
            client.println("on");
          }    
          else if(relay1State == HIGH){
            client.println("off");                                                                      
          }
          client.println("<br><br>");
          
          client.println("<a href=\"/relay1on\"><button>ON</button></a>");
          client.println("<a href=\"/relay1off\"><button>OFF</button></a>");
          
          client.println("</CENTER>");
          client.println("</BODY>");
          client.println("</HTML>");
          
    delay(1);
    // close the connection:
    client.stop();
    Serial.println("client disonnected");
 }
