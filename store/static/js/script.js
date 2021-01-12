function hidePlusButton() {
    $(".add-quantity").hide();
}

funtion toggler(divId) {
    var tempId = divId.slice(-1);
       var x = document.getElementById("icon" + tempId);
       var y = document.getElementById("cardHeader" + tempId);
       x.style.display = "none";
       y.style.visibility = "visible";
       $("#delBtn_" + tempId).show();
       $("#" + divId).toggle();
   }
}