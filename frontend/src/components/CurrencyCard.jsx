import {Card} from "antd";

function CurrencyCard(prop) {
    const { currency } = prop
    let price = (currency.quote.USD.price).toFixed(2)
    let difference = (currency.quote.USD.percent_change_24h).toFixed(2)
    return (
        <Card
            title={
                <div className="flex items-center gap-3">
                    <img alt = {`Image of ${currency.name}`} src={`https://s2.coinmarketcap.com/static/img/coins/64x64/${currency.id}.png`}/>
                    <span>{currency.name}</span>
                </div>
            }

            style={{
                width: 300,
            }}
        >
            <p>Cryptocurrency: {currency.name}</p>
            <p>Current price: {price}</p>
            <p>Percent difference in 24 hour:
                {difference >= 0 ? <span className="text-green-500"> +{difference}%</span> :
                    <span className="text-red-500"> {difference}%</span>
                }
            </p>
        </Card>
    )
}

export default CurrencyCard
