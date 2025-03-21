import { useRoute } from "wouter";
import { vehicles } from "@/lib/mockData";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Users, Briefcase, GaugeCircle, Calendar, MapPin } from "lucide-react";

export default function VehicleDetails() {
  const [, params] = useRoute("/vehicle/:id");
  const vehicle = vehicles.find((v) => v.id === params?.id);

  if (!vehicle) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-900">Vehicle not found</h1>
          <p className="text-gray-600 mt-2">The requested vehicle does not exist.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
        <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv8VCDlM64uFv7274Mn3UjHpqXRGtIwAWokg&s"
            alt="Rent logo"
            className="h-12"
          />
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-12 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div>
            <img
              src={vehicle.image}
              alt={vehicle.name}
              className="w-full aspect-video object-cover rounded-lg shadow-lg"
            />
          </div>
          
          <Card className="p-6">
            <div className="mb-6">
              <h1 className="text-3xl font-bold text-gray-900">{vehicle.name}</h1>
              <p className="text-lg text-gray-600 mt-2">{vehicle.description}</p>
            </div>

            <div className="grid grid-cols-2 gap-4 mb-8">
              <div className="flex items-center gap-2">
                <Users className="h-5 w-5 text-primary" />
                <span>{vehicle.capacity} seats</span>
              </div>
              <div className="flex items-center gap-2">
                <Briefcase className="h-5 w-5 text-primary" />
                <span>{vehicle.luggage} bags</span>
              </div>
              <div className="flex items-center gap-2">
                <GaugeCircle className="h-5 w-5 text-primary" />
                <span>{vehicle.transmission}</span>
              </div>
              <div className="flex items-center gap-2">
                <Calendar className="h-5 w-5 text-primary" />
                <span>Free cancellation</span>
              </div>
            </div>

            <div className="border-t pt-6">
              <div className="flex justify-between items-center mb-6">
                <div>
                  <span className="text-3xl font-bold">${vehicle.price}</span>
                  <span className="text-gray-600"> / day</span>
                </div>
                <Button size="lg">Reserve Now</Button>
              </div>
            </div>
          </Card>
        </div>
      </main>
    </div>
  );
}
