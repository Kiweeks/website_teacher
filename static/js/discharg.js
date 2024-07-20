const getCodeBtn = document.getElementById("bt_load_file");
const postCodeBtn = document.getElementById("bt_download");
const codeInput = document.getElementById("bt_delete");

bt_load_file.addEventListener("click", () => {
    const file = document.getElementById("file");

    fetch('/load-file-admin', {
        method: 'post',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
        body: JSON.stringify({
            data: file
          })
    })
    .then((response) => response.json())
    .then((data) => alert(data.message));

    location.reload();
});