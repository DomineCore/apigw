import http from '@/api/http'

const apiresource = {
    namespaced: true,
    actions: {
        // 加载api数据
        loadApiResource({ commit }, params) {
            return http.get('/api/v1/apiresource/',params).then(response => response)
        },
        // api接入
        createApiResource({ commit }, data){
            console.log(data)
            return http.post('/api/v1/apiresource/',data).then(response => response)
        }
    }
}

export default apiresource
