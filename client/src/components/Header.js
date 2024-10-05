// header component

export default function Header() {
    return (
        <div className="bg-white shadow-md">
            <header className="flex justify-between items-center p-4">
                <div className="flex items-center">
                    {/* Logo Placeholder */}
                    <div className="text-2xl text-blue-600">
                        <span role="img" aria-label="Medical symbol">🏥</span> {/* Emoji as a logo */}
                        <span className="ml-2">Diagnosify</span>
                    </div>
                </div>
            </header>
        </div>
    );
}