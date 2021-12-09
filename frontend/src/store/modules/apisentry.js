import http from '@/api/http'

const apisentry = {
    namespaced: true,
    actions: {
        // 加载api异常记录
        loadApiSentry({ commit }, params) {
            return http.get('/api/v1/apisentry/',params).then(response => response)
        },
    }
}

export default apisentry
