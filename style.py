body{
    font-family: Arial, sans-serif;
    background: linear-gradient(to left, #eaf4fb, #f8fbfd);
    margin: 0;
    direction: rtl;
    color: #2c3e50;
}

.topbar{
    background: linear-gradient(to left, #2E86DE, #5DADE2);
    color: white;
    padding: 20px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    box-shadow: 0 3px 12px rgba(0,0,0,0.12);
    animation: fadeDown 0.8s ease;
}

.container{
    width: 90%;
    max-width: 1100px;
    margin: 30px auto;
}

.login-page{
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(to left, rgba(46,134,222,0.08), rgba(93,173,226,0.03));
}

.login-box{
    width: 400px;
    background: white;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.12);
    text-align: center;
    animation: fadeUp 0.8s ease;
}

.logo{
    width: 90px;
    height: 90px;
    object-fit: contain;
    margin-bottom: 10px;
}

.login-box h2{
    margin-bottom: 8px;
    color: #2E86DE;
}

.login-subtitle{
    color: #7f8c8d;
    margin-bottom: 20px;
    font-size: 14px;
}

label{
    display: block;
    text-align: right;
    margin-top: 10px;
    margin-bottom: 6px;
    font-weight: bold;
}

input{
    width: 100%;
    padding: 12px;
    margin-bottom: 12px;
    border: 1px solid #d5d8dc;
    border-radius: 12px;
    box-sizing: border-box;
    background: #fbfcfc;
    transition: 0.3s;
    font-size: 15px;
}

input:focus{
    border-color: #2E86DE;
    outline: none;
    box-shadow: 0 0 6px rgba(46,134,222,0.25);
    transform: scale(1.01);
}

button{
    width: 100%;
    padding: 12px;
    background: linear-gradient(to left, #2E86DE, #5DADE2);
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s;
}

button:hover{
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(46,134,222,0.25);
}

.card{
    background: white;
    padding: 24px;
    margin-bottom: 20px;
    border-radius: 18px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.08);
    animation: fadeUp 0.7s ease;
}

.dashboard-grid{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
}

.stat-box{
    background: linear-gradient(to left, #ffffff, #f9fcfe);
    border-right: 5px solid #2E86DE;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 5px 14px rgba(0,0,0,0.06);
    transition: 0.3s;
}

.stat-box:hover{
    transform: translateY(-4px);
}

.stat-box h3{
    margin: 0 0 10px;
    color: #2E86DE;
    font-size: 18px;
}

.stat-box p{
    margin: 0;
    font-size: 22px;
    font-weight: bold;
    color: #34495e;
}

.btn{
    background: #48C9B0;
    padding: 11px 16px;
    color: white;
    text-decoration: none;
    border-radius: 10px;
    margin-left: 10px;
    margin-top: 10px;
    display: inline-block;
    transition: 0.3s;
    font-size: 15px;
}

.btn:hover{
    transform: translateY(-2px);
    opacity: 0.95;
}

.btn-danger{
    background: #e74c3c;
}

.error{
    color: #c0392b;
    background: #fadbd8;
    padding: 12px;
    border-radius: 10px;
    text-align: center;
    font-weight: bold;
    margin-top: 15px;
    animation: shake 0.3s ease;
}

.success{
    color: #1e8449;
    background: #d5f5e3;
    padding: 12px;
    border-radius: 10px;
    text-align: center;
    font-weight: bold;
    margin-top: 15px;
}

.page-title{
    color: #2E86DE;
    margin-bottom: 15px;
}

.hero-image{
    width: 100%;
    max-height: 240px;
    object-fit: cover;
    border-radius: 16px;
    margin-top: 20px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
}

.icon{
    margin-left: 6px;
    font-size: 16px;
}

.welcome-box{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
    flex-wrap: wrap;
}

.badge{
    background: #ebf5fb;
    color: #2E86DE;
    padding: 8px 14px;
    border-radius: 30px;
    font-weight: bold;
}

@keyframes fadeUp{
    from{
        opacity: 0;
        transform: translateY(18px);
    }
    to{
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeDown{
    from{
        opacity: 0;
        transform: translateY(-18px);
    }
    to{
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes shake{
    0%{ transform: translateX(0); }
    25%{ transform: translateX(4px); }
    50%{ transform: translateX(-4px); }
    75%{ transform: translateX(4px); }
    100%{ transform: translateX(0); }
}
