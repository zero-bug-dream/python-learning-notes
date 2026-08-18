const chatBox = document.getElementById("chatBox");
const chatInput = document.getElementById("chatInput");
const btnSend = document.querySelector(".btn-send");
const btnNewGame = document.querySelector(".btn-top-action");
const btnStart = document.querySelector(".btn-control");

// 保存当前会话ID
let currentSessionId = null;

// 动态追加聊天气泡函数
function addMessage(text, isAi) {
    const row = document.createElement("div");
    row.className = "msg-row " + (isAi ? "msg-ai" : "msg-user");

    const bubble = document.createElement("div");
    bubble.className = isAi ? "bubble ai-bubble" : "bubble user-bubble";
    bubble.innerText = text;

    const avatar = document.createElement("div");
    avatar.className = "avatar";
    avatar.innerText = isAi ? "AI" : "你";

    if(isAi){
        row.appendChild(avatar);
        row.appendChild(bubble);
    }else{
        row.appendChild(bubble);
        row.appendChild(avatar);
    }
    chatBox.appendChild(row);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// ===== 新建会话接口 POST /api/sessions =====
async function createNewSession(){
    try {
        console.log("开始请求新建会话");
        const res = await fetch("/api/sessions", {
            method: "POST"
        });
        const resp = await res.json();
        console.log("后端完整返回：", resp);
        // 你的后端包装了ApiResponse，id在resp.data
        currentSessionId = resp.data;
        console.log("赋值后的currentSessionId =", currentSessionId);
        chatBox.innerHTML = "";
    }catch(err){
        console.error("创建会话异常",err);
        addMessage("创建会话失败，请检查后端服务", true);
    }
}
// ===== 发送聊天消息接口 POST /api/chat =====
async function sendToApi(userText){
    addMessage(userText, false);
    chatInput.value = "";

    if(!currentSessionId){
        addMessage("会话未初始化，请新建游戏", true);
        return;
    }

    try {
        const resp = await fetch("/api/chat", {
            method:"POST",
            headers:{"Content‑Type":"application/json"},
            body: JSON.stringify({
                message: userText,
                session_id: currentSessionId
            })
        })
        const jsonRes = await resp.json();
        // jsonRes = {code:200, message:"ok", data:{reply:"xxx"}}
        const aiReply = jsonRes.data.reply;
        addMessage(aiReply, true);
    }catch(err){
        addMessage("网络出错，请重试",true);
        console.error(err);
    }
}
// 发送按钮点击
btnSend.addEventListener("click", ()=>{
    const text = chatInput.value.trim();
    if(text) sendToApi(text);
})

// 回车发送
chatInput.addEventListener("keydown",e=>{
    if(e.key === "Enter"){
        const text = chatInput.value.trim();
        if(text) sendToApi(text);
    }
})

// 页面加载完毕，自动创建会话
window.onload = async ()=>{
    await createNewSession();
}

// 点击【新建游戏】按钮，重新生成新会话
btnNewGame.addEventListener("click", async ()=>{
    await createNewSession();
})

// 点击【开始游戏】按钮，新建会话
btnStart.addEventListener("click", async ()=>{
    await createNewSession();
})