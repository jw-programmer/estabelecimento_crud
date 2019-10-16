function getHeaders() {
    const token = localStorage.getItem('token');
    return {
        'Content-Type': 'application/json',
        ...token && {
            'Authorization': `Bearer ${token}`
        }
    };
}

export default getHeaders;