*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekansalasana3
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  aino  kissa555!
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  ok  kissa555!
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  jee!  kissa555!
    Output Should Contain  Username is not valid

Register With Valid Username And Too Short Password
    Input Credentials  moikka  kissa5
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  elisa  salainensalasana
    Output Should Contain  Password must include characters another than letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  aino  salasana11

