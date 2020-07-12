//TODO Find how to save data with a JSON file.
function JSONFile(string)
{
    if(string == "Create")
        {
        var User_List = '{ "users" : [' +
        '{ "name":"Sama" , "lastname":"Filipi" , "username":"apnea_deepDiver", "email":"investigate_this_guy@apneapro.com" , "password":"loveTheSea123", "ID_User":"3"} ]}';
        var obj = JSON.parse(User_List); 
        } 
    else
    {

    }
    return obj;
}

function validateUser() //Checks if the password and the user name both match inside the JSON file.
{
    var obj = JSONFile("Create");

    if(obj.users[0].username == document.getElementById("txt_username_login").value && obj.users[0].password == document.getElementById("txt_password_login").value)
    {
        console.log("The user and the password have been validated.");
    }
    else
    {
        console.log("This password does not match with any username stored in the JSON.")
    }
}
function CreateNewUsers()
{
    var obj = JSONFile();
    obj.users.append()
}

function onLoad()
{
    //Setting a template for the array.
    var User_List = '{ "users" : [' +
    '{ "name":"Sama" , "lastname":"Filipi" , "username":"apnea_deepDiver", "email":"investigate_this_guy@apneapro.com" , "password":"loveTheSea123", "ID_User":"3"} ]}';
    var obj = JSON.parse(User_List); 

    //Filling the drop-down with the first option. Empty. 
    var option = document.createElement("option");
    option.User_List = obj.users[0].ID_User;
    dropdown.add(option);

    //! Testing tool, please remove later.
    console.log(obj.users[0].ID_User)
}
