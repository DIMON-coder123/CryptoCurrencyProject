import {Button, Divider, Menu, Space, Spin} from 'antd';
import axios from "axios";
import {useEffect, useState} from "react";
import CurrencyCard from "./components/CurrencyCard.jsx";

function getItem(label, key, icon, children, type) {
    return {
        key,
        icon,
        children,
        label,
        type,
    };
}

const App = () => {

    const [currencies, setCurrencies] = useState([]);
    const [currencyId, setCurrencyId] = useState(1);
    const [currencyInfo, setCurrencyInfo] = useState(null);



    const getCurrencies = () => {
        axios.get('http://127.0.0.1:8000/cryptocurrencies').then((r) => {
            const currenciesResponse = r.data
            const menuItem = [
                getItem("Cryptocurrency list", 'g1', null,
                    currenciesResponse.map((item) => {
                        return {label: item.name, key: item.id};
                    }), 'group'
                )
            ]
            setCurrencies(menuItem)
        })
    }


    const getParticularCurrency = () => {
        axios.get(`http://127.0.0.1:8000/cryptocurrencies/${currencyId}`).then((r) => {
            setCurrencyInfo(r.data);
        })
    }


    useEffect(() => {
        getCurrencies()
    }, []);


    useEffect(() => {
        setCurrencyInfo(null)
        getParticularCurrency()
    }, [currencyId]);


    const onClick = (e) => {
        setCurrencyId(e.key)
    };
    return (
        <div>
            <div className="flex justify-end my-0.5 mx-3">
                <Space className="flex items-center">
                    <Button color="primary" variant="filled" >Log in</Button>
                    <Button type="primary" variant="filled">Sign up</Button>

                </Space>
            </div>
            <Divider style={{borderColor: "#91caff"}}></Divider>

            <div className="flex">
                <Menu
                    onClick={onClick}
                    style={{
                        width: 256,
                    }}
                    defaultSelectedKeys={['1']}
                    defaultOpenKeys={['sub1']}
                    mode="inline"
                    items={currencies}
                    className={"h-screen overflow-scroll"}
                />
                <div className="mx-auto my-auto">
                    {currencyInfo ? <CurrencyCard currency={currencyInfo} /> : <Spin/>}
                </div>
            </div>
        </div>

    );

};
export default App;