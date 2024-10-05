import Description from "../components/Description";
import Header from "../components/Header";
import SearchableDropdown from "../components/SearchableDropdown";

function App() {
  return (
    <div className="font-robotoMono">
      <Header />
      <div className="py-10">
        <Description />
        <SearchableDropdown />
      </div>
    </div>
  );
}

export default App;
