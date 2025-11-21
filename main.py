from pyscript import display

clubs = {
    "Dance Club": {
        "Name": "Dance Club",
        "Description": "A club for students who like dancing.",
        "Meeting Time": "Monday & Thursday 3-5 PM",
        "Location": "Dance Room",
        "Moderator": "Mr. Marutani",
        "Members": 25
    },
    "COCC Club": {
        "Name": "COCC Club",
        "Description": "A leadership training club.",
        "Meeting Time": "Thursday 3-5 PM",
        "Location": "Quadrangle",
        "Moderator": "Ms. Mobilla",
        "Members": 25
    },
    "Glee Club": {
        "Name": "Glee Club",
        "Description": "A club for students who enjoy singing.",
        "Meeting Time": "Monday & Friday 3-5 PM",
        "Location": "Music Room",
        "Moderator": "Ms. Loyola",
        "Members": 25
    }
}


def show_club(event):

    club_name = document.getElementById("clubDropdown").value
    info = clubs[club_name]

    document.getElementById("output").innerHTML = ""

    display("Name: " + info["Name"], target="output")
    display("Description: " + info["Description"], target="output")
    display("Meeting Time: " + info["Meeting Time"], target="output")
    display("Location: " + info["Location"], target="output")
    display("Moderator: " + info["Moderator"], target="output")
    display("Members: " + str(info["Members"]), target="output")
