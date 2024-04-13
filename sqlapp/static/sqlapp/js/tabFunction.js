
function openTab(evt, tabName) {
 let tabElement = document.getElementById(tabName);
    // エレメントが存在しない場合のエラーハンドリング
    if (!tabElement) {
        console.error("Element not found: " + tabName);
        return;
    }
    
    let i, tabcontent, tablinks;

    // すべてのタブコンテンツを非表示
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // すべてのタブのアクティブ状態を解除
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // クリックされたタブのコンテンツを表示し、アクティブ状態にする
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";

    // クリックされたタブの背景色を取得
    let activeTab = evt.currentTarget;
    let activeTabColor = window.getComputedStyle(activeTab, null).backgroundColor;

    // 対応するタブコンテンツに背景色を適用
    document.getElementById(tabName).style.backgroundColor = activeTabColor;
}
