import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: "0.0.0.0",  // 允许外部访问
    port: 5173,       // 指定端口
    strictPort: true, // 若端口被占用则报错
    open: false,      // 是否自动打开浏览器
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
        rewrite: (p) => p.replace(/^\/api/, ""),
      }
    }
  }
})
