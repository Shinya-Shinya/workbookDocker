function truncateString(str, num) {
    if (str.length > num) {
        return str.slice(0, num) + "...";
    } else {
        return str;
    }
}
    document.getElementById("id_shoseki").addEventListener("change", function() {
        var selectedShoseki = this.value;
        fetch(`/get-previous-registration-data/?shoseki=${selectedShoseki}`)
            .then(response => response.json())
            .then(data => {
                if (data.touroku1tsumaeShoseki) {
                    document.getElementById("touroku1tsumaeShoseki").textContent = `【${truncateString(data.touroku1tsumaeShoseki, 40)}】`;
                    document.getElementById("touroku1tsumaeQuestion").textContent = truncateString(data.touroku1tsumaeQuestion, 40);
                    document.getElementById("touroku1tsumaePage").textContent = `(${data.touroku1tsumaePage})`;
                } else if (data.message) {
                    // 書籍に関連するデータがない場合の処理
                    document.getElementById("touroku1tsumaeShoseki").textContent = data.message;
                    document.getElementById("touroku1tsumaeQuestion").textContent = "";
                    document.getElementById("touroku1tsumaePage").textContent = "";
                } else {
                    // データが見つからない場合の処理
                    document.getElementById("touroku1tsumaeShoseki").textContent = "登録データはありません。";
                    document.getElementById("touroku1tsumaeQuestion").textContent = "";
                    document.getElementById("touroku1tsumaePage").textContent = "";
                    var detailLink = document.querySelector('.prevData a');
                    if (detailLink) {
                        detailLink.style.display = 'none';
                    }
                }
            });
        });