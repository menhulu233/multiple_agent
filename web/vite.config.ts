import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import {ElementPlusResolver} from 'unplugin-vue-components/resolvers'
import {viteMockServe} from "vite-plugin-mock";
// https://vite.dev/config/
export default defineConfig(({command}) => {
    return {
        plugins: [
            vue(),
            AutoImport({
                resolvers: [ElementPlusResolver()],
            }),
            Components({
                resolvers: [ElementPlusResolver()],
            }),
            viteMockServe({
                mockPath: "src/mock",//设置mock文件存储目录
                enable: command=="serve",//设置是否启用本地mock文件
                watchFiles: true,//设置是否监视mockPath对应的文件夹内文件中的更改
                logger: true,//是否在控制台显示请求日志
            }),
        ],

    }
})
