// awesome everything seems to work
// create seperate endpoints for all sensors (voltage,current,VFD)
#include <WiFi.h>
#include <WiFiMulti.h>
#include <ArduinoJson.h>
#include <Arduino.h>
#include<pthread.h>

//#include <WiFi.h>
//#include <WiFiMulti.h>

#include <HTTPClient.h>

#define USE_SERIAL Serial
#define MYSERVER "http://balarubinan.pythonanywhere.com/"
// used for setting standby value
#define LINEAR_END "http://balarubinan.pythonanywhere.com/lin/"
#define LINEAR_GET "http://balarubinan.pythonanywhere.com/lin/123"

// used for setting actual live readings
#define ROT_END "http://balarubinan.pythonanywhere.com/rot"
#define ROT_GET "http://balarubinan.pythonanywhere.com/rot/123"

#define VFD_VOL "http://balarubinan.pythonanywhere.com/vfdvol"

#define VFD_CUR "http://balarubinan.pythonanywhere.com/vfdcur"
#define VFD_CNTRL "http://balarubinan.pythonanywhere.com/vfdcntrl"



#define MYPASS "1234567899"
WiFiMulti wifiMulti;

WiFiMulti WiFiMulti;
int cnt=0;
//("balarubinan", "12345678999")

void connect_wifi(const char*,const char*);
void setup()
{
    Serial.begin(9600);
    Serial.println("Sericla connnecttion setp");
    connect_wifi("balarubinan", "12345678999");
    Serial.println("Wifi setup complete");
}

void connect_wifi(const char* ssid,const char* pass)
{
    Serial.println("before add AP");
    WiFiMulti.addAP(ssid,pass);
    Serial.println();
    Serial.println("Waiting for WiFi... ");

    while(WiFiMulti.run() != WL_CONNECTED) {
        Serial.println("in wifi loop");
        delay(500);
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());

    delay(500);
}

// make a HTTP Get request
String httpGETRequest(const char* serverName) {
  HTTPClient http;

  // Your IP address with path or Domain name with URL path
  http.begin(serverName);

  // Send HTTP POST request
  int httpResponseCode = http.GET();

  String payload = "{}";

  if (httpResponseCode>0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    payload = http.getString();
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  // Free resources
  http.end();

  return payload;
}

// Makes a HTTP post request
void httpPOSTRequest(const char* serverName,String load=""){
   HTTPClient http;

  // Your IP address with path or Domain name with URL path
    http.begin(serverName+load); // either this
    http.addHeader("Content-Type", "text/plain");
    int httpResponseCode=-1;
    if(load==""){
      Serial.print("normal mode");
      httpResponseCode=http.POST("-1");
    }
    else{
      Serial.println("Load mode");
      httpResponseCode=http.POST(load); //or this is working
    }
    if (httpResponseCode>0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  // Free resources
  http.end();
}

// parses string format payload to JSONVr format object
//JSONVar parse_JSON(String payload){
//  JSONVar myObject = JSON.parse(payload);
//  JSONVar none;
//
//// JSON.typeof(jsonVar) can be used to get the type of the var
//if (JSON.typeof(myObject) == "undefined") {
//  Serial.println("Parsing input failed!");
//  return none;
//}
//
//Serial.print("JSON object = ");
//Serial.println(myObject);
//return(myObject);
//}

// read analog values and return digital value
// ADC function to conect with rasperry PI
void ADC_converter(int read_pin,int digi_pin)
{
  float value=analogRead(digi_pin);
//  finsih this part
}

// reads the number of pulses and sends it as post request to endpoint in flask
// define /rot endpoint in flask api
// this function runs as a thread continously
void rotary_reader(int ip_pin){
  while(true){
    if(digitalRead(ip_pin)==HIGH){ // check if this condition works
      cnt++;
  }
}}

void rotary_encoder()
{
    // start the rotary_reader thread here
    while(true){
        httpPOSTRequest(ROT_END,String(cnt));
        cnt=0;
        sleep(1000);
    }
}

// sends the acttual voltage
// needs two endpoint /standby_init -> to intialse standby voltage
// /linear_vol -> actual live voltage values of linear encoder
void linear_encoder(int ip_pin)
{
  Serial.println("in Linear function");
  float stand_by_voltage=analogRead(ip_pin);
  // sending standby voltage
//  httpPOSTRequest(LINEAR_END,String(stand_by_voltage));
//  httpPOSTRequest(LINEAR_END,"reset");
  while(true){
//    for(int i=1;i<30;i++){
    Serial.println("Before loop");
    float val=analogRead(ip_pin);
    Serial.println("The value of pin voltage: pin number ");
//    Serial.println(i);
    Serial.print(val/1241);
    Serial.println(" Volts");
    delay(1000);
//    }
    //sending actual values read live
//    sleep(1000);
    httpPOSTRequest(LINEAR_END,String(val));
  }
}
void loop()
{
  static int num=0;
  Serial.println("Loop start");
//  String output=httpGETRequest(LINEAR_GET);
// ADC is pin 15
//  linear_encoder(15);
  httpPOSTRequest(LINEAR_END,String(num+2));
//  Serial.println(output);
//  Serial.println(parse_JSON(output));
  Serial.println("Code done");
//   http.begin("http://balarubinan.pythonanywhere.com/1"); //HTTP
}