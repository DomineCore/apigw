import service from './service'

const http ={
    get(url,params){
        const config = {
            method: 'get',
            url:url
        }
        if(params) config.params = params
        console.log(config)
        return service(config)
    },
    post(url,params){
        const config = {
            method: 'post',
            url:url
        }
        console.log(config)
        if(params) config.data = params
        return service(config)
    },
    put(url,params){
        const config = {
            method: 'put',
            url:url
        }
        if(params) config.params = params
        return service(config)
    },
    delete(url,params){
        const config = {
            method: 'delete',
            url:url
        }
        if(params) config.params = params
        return service(config)
    }
}
//暴露
export default http
