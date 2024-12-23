import axios from 'axios';

const request = axios.create({
    baseURL: 'http://localhost:5173/',
    timeout: 10000, // 请求超时时间
    headers: {'Content-Type': 'application/json'}
});

export default request;
