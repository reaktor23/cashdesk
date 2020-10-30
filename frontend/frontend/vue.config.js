module.exports = {
    outputDir: "dist",
    devServer: {
        writeToDisk: true,
        proxy: {
            '/api': {
                target: 'http://localhost:8010',
                ws: true,
                changeOrigin: true
            },
        }
    },
    transpileDependencies: ["vuetify"]
};
