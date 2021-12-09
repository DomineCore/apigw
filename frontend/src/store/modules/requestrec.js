import http from '@/api/http'

const requestrec = {
    namespaced: true,
    actions: {
        // 加载调用记录
        loadRequestRec({ commit }, params) {
            return http.get('/api/v1/requestrec/',params).then(response => response)
        },
    }
}

export default requestrec
