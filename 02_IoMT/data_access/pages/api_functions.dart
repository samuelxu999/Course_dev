// Importing necessary libraries and packages
import 'dart:convert';
import 'package:http/http.dart' as http;

Future<String> getHW() async {
  final url=Uri.parse('https://76zlh8kr8d.execute-api.us-east-2.amazonaws.com/test/Test');
  final response = await http.post(url,
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8'
    },
    body: jsonEncode(<String,String>{"payload":"This is a test message from flutter."})
  );
  if(response.statusCode == 200) {
    // inline example to process json data
    Map<String,dynamic> mapbody = jsonDecode(response.body);
    String bodyvalue=mapbody['body'];

    Map<String,dynamic> mapmsg = jsonDecode(bodyvalue);
    String mapvalue=mapmsg['payload'];

    return mapvalue;  
  }
  else{
    throw Exception('Fail to access hello world.');
  }
}

// class Steps {
//   String dataTime;
//   String value;

//   Steps.fromJson(Map<String, dynamic> json):
//         dataTime =json['dataTime'],
//         value = json['value'];
// }

Future<String> getSteps(String startdate, String enddate) async {
  final url=Uri.parse('https://9xgokmzozd.execute-api.us-east-2.amazonaws.com/test/getSteps');
  final response = await http.post(url,
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8'
    },
    body: jsonEncode(<String,String>{
      "access_token": "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1BYSjYiLCJzdWIiOiJCTjRXTUwiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJlY2cgcnNldCByaXJuIHJveHkgcnBybyBybnV0IHJzbGUgcmNmIHJhY3QgcnJlcyBybG9jIHJ3ZWkgcmhyIHJ0ZW0iLCJleHAiOjE3Mzk0MzIzMjUsImlhdCI6MTczOTQwMzUyNX0.m19kFGCttJsU0hpfL940Drfu6XA6tnHchrXxsavbmss",
      "startdate": startdate,
      "enddate": enddate
    })
  );
  if(response.statusCode == 200) {
    // print(response.body);
    Map<String,dynamic> mapbody = jsonDecode(response.body);
    // print(mapbody);
 
    List<dynamic> ls_value = jsonDecode(mapbody['body']);
    // print(ls_value[0].runtimeType);
    // print(ls_value);
    
    Map<String,dynamic> _data =ls_value[0];
    // print(_data['dateTime']);
    // print(_data['value']);
    return mapbody['body'];  
  }
  else{
    throw Exception('Fail to get data.');
  }
}