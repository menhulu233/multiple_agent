import request from "../utils/request.ts";

const login=()=>{
    request.post(
        "/api/user/login",
        {
            username:"admin",
            password:"123456"
        }
    ).then(res=>{
        console.log(res)
        return res
    }).catch(err=>{
        console.log(err)
        return "请求错误"
    })
}
export default login