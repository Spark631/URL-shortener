function copy() {
    var copyText = document.getElementById("link1").innerHTML;

    navigator.clipboard.writeText(copyText);
    
    swal({
        title: "Sucessful!",
        text: "Link copied to clipboard",
        icon: "success",
        button: "Continue",
    })
}