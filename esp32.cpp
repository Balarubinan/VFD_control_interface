/*
 *  This sketch sends a message to a TCP server
 *
 */
// create seperate endpoints for all sensors (voltage,current,VFD)
// check if all the POST requests work in the board!!1
#include <WiFi.h>
#include <WiFiMulti.h>
#include <Arduino_JSON.h>
#include <Arduino.h>
#include<thread.h>

//#include <WiFi.h>
//#include <WiFiMulti.h>

#include <HTTPClient.h>

#define USE_SERIAL Serial
#define MYSERVER "http://balarubinan.pythonanywhere.com/1"
#define LINEAR_END "http://balarubinan.pythonanywhere.com/lin"
// used for setting actual live readings
#define ROT_END "http://balarubinan.pythonanywhere.com/rot"
#define VFD_END "http://balarubinan.pythonanywhere.com/vfdcntrl"



#define MYPASS "1234567899"
WiFiMulti wifiMulti;

WiFiMulti WiFiMulti;
int cnt=0;
//("balarubinan", "12345678999")

void connect_wifi(const char*,const char*);
void setup()
{
    Serial.begin(9600);
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
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");
    int httpResponseCode=-1;
    if(load==""){
      Serial.print("normal mode");
      httpResponseCode=http.POST("{\"reading\":\"from board\"}");
    }
    else{
      httpResponseCode=http.POST(load);
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
JSONVar parse_JSON(String payload){
  JSONVar myObject = JSON.parse(payload);
  JSONVar none;

// JSON.typeof(jsonVar) can be used to get the type of the var
if (JSON.typeof(myObject) == "undefined") {
  Serial.println("Parsing input failed!");
  return none;
}

Serial.print("JSON object = ");
Serial.println(myObject);
return(myObject);
}

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
}

void rotary_encoder()
{
    // start the rotary_reader thread here
    while(true){
        Serial.println("Value of count is ");
        Serial.println(cnt);
        httpPOSTRequest(ROT_END,"{\"rot\":"+String(cnt)+"}");
        cnt=0;
        sleep(1000);
    }
}

// sends the acttual voltage
// needs two endpoint /standby_init -> to intialse standby voltage
// /linear_vol -> actual live voltage values of linear encoder
void linear_encoder(int ip_pin)
{
  float stand_by_voltage=analogRead(ip_pin);
  // sending standby voltage
  httpPOSTRequest(LINEAR_END,"{\"reading\""+String(stand_by_voltage)+"}");
  httpPOSTRequest(LINEAR_END,"{\"reading\":\"reset\"}")
  while(true){
    float val=analogRead(ip_pin);
    //sending actual values read live
    sleep(1000)
    httpPOSTRequest(LINEAR_END,"{\"reading\":"+String(val)+"}");
  }
}
void loop()
{
  Serial.println("Loop start");
//  String output=httpGETRequest(MYSERVER);
  httpPOSTRequest(MYSERVER);
//  Serial.println(output);
//  Serial.println(parse_JSON(output));
  Serial.println("Code done");
//   http.begin("http://balarubinan.pythonanywhere.com/1"); //HTTP
}